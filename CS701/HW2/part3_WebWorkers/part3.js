(function () {
    window.onload = init;

    var startButton;
    var accumulatedResult = 0;
    var storage = [];

    function init() {
        startButton = document.getElementById("startButton");
        startButton.onclick = sendDataToWorkers;
    }

    // Complete the following code

    // Handle messages received from the Web Worker
    function handleReceipt(event) {
        // prints items under received messages
        var itemsList = document.getElementById("items");
        var messages = document.createElement("li");
        var result = JSON.stringify(event.data);
        messages.innerHTML = result;
        itemsList.appendChild(messages);

        // prints sum result
        accumulatedResult + event.data.result;
        var output = document.getElementById("sum");
        output.innerHTML = accumulatedResult + event.data.result;

        storage.push(event.data); // adds data to array

        // prints items under stored messages
        var itemsList = document.getElementById("storageItems");
        var storedMessages = document.createElement("li");
        var json = JSON.stringify(storage);
        var key = "storedMessages";
        window.localStorage.setItem(key, json);
        storedMessages.innerHTML = result;
        itemsList.appendChild(storedMessages);
    }

    // Complete the following code

    // send messages to the Web Workers
    function sendDataToWorkers(e) {
        // startButton.disabled = true;

        let range = document.getElementById("range").value; // gets range value 
        let numWorkers = document.getElementById("numWorkers").value; // gets number of workers
        let partition = range / numWorkers;

        // loop through number of workers and calls the worker
        for (var i = 1; i <= numWorkers; i++) {
            let myWorker = new Worker("computeWorker.js");

            myWorker.onmessage = handleReceipt;
            myWorker.postMessage({ index: i - 1, start: 1 + partition * (i - 1), end: partition * i });
        }
    }

    // Feel free to add any helper methods
})();
