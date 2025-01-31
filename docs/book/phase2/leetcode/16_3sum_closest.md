<textarea id="code" rows="5" cols="50">print("Hello, GitHub Pages!")</textarea><br>
<button onclick="runPython()">Run</button>
<pre id="output"></pre>

<script src="https://cdn.jsdelivr.net/pyodide/v0.23.4/full/pyodide.js"></script>
<script>
    async function loadPyodideAndRun() {
        window.pyodide = await loadPyodide();
    }
    loadPyodideAndRun();

    async function runPython() {
        let code = document.getElementById("code").value;
        let outputElement = document.getElementById("output");
        try {
            let result = await pyodide.runPythonAsync(code);
            outputElement.textContent = result;
        } catch (error) {
            outputElement.textContent = "Error: " + error;
        }
    }
</script>