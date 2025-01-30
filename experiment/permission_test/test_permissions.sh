#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

check_permission() {
    local file=$1
    local expected=$2
    local desc=$3
    
    echo "Testing $desc ($file)..."
    
    # Test read permission
    if echo "$expected" | grep -q "r"; then
        if cat "$file" >/dev/null 2>&1; then
            echo -e "${GREEN}✓ Can read $file (Expected)${NC}"
        else
            echo -e "${RED}✗ Cannot read $file (Should be readable)${NC}"
            return 1
        fi
    else
        if cat "$file" >/dev/null 2>&1; then
            echo -e "${RED}✗ Can read $file (Should not be readable)${NC}"
            return 1
        else
            echo -e "${GREEN}✓ Cannot read $file (Expected)${NC}"
        fi
    fi
    
    # Test write permission
    if echo "$expected" | grep -q "w"; then
        if echo "test" 2>/dev/null >>"$file"; then
            echo -e "${GREEN}✓ Can write to $file (Expected)${NC}"
        else
            echo -e "${RED}✗ Cannot write to $file (Should be writable)${NC}"
            return 1
        fi
    else
        if echo "test" 2>/dev/null >>"$file"; then
            echo -e "${RED}✗ Can write to $file (Should not be writable)${NC}"
            return 1
        else
            echo -e "${GREEN}✓ Cannot write to $file (Expected)${NC}"
        fi
    fi
    
    # Test execute permission
    if echo "$expected" | grep -q "x"; then
        if [ -x "$file" ]; then
            echo -e "${GREEN}✓ Can execute $file (Expected)${NC}"
        else
            echo -e "${RED}✗ Cannot execute $file (Should be executable)${NC}"
            return 1
        fi
    else
        if [ -x "$file" ]; then
            echo -e "${RED}✗ Can execute $file (Should not be executable)${NC}"
            return 1
        else
            echo -e "${GREEN}✓ Cannot execute $file (Expected)${NC}"
        fi
    fi
    
    echo "----------------------------------------"
    return 0
}

# Test each file
echo "Testing file permissions..."
echo "----------------------------------------"

check_permission "read_only.sh" "r" "read-only file"
check_permission "write_only.sh" "w" "write-only file"
check_permission "execute_only.sh" "x" "execute-only file"
check_permission "read_write.sh" "rw" "read-write file"
check_permission "read_execute.sh" "rx" "read-execute file"
