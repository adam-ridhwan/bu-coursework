(function () {
    window.onload = init;

    var sourceId; // holds the data for dragged item
    var droppedList = []; // holds the senators who voted

    function init() {
        var key = JSON.parse(window.localStorage.getItem("senators"));
        if (key == "" || key == null) {
            // call ajax function
            ajaxCall();
        } else {
            // call local storage function
            displayFromLocalStorage(key);
        }
    }

    // ajax function when page is fresh with no data in local storage
    function ajaxCall() {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function () {
            if (this.readyState == 4) {
                if (this.status == 200 || this.status == 0) {
                    ajaxState(this);
                }
            }
        };
        xmlhttp.open("GET", "partyList.xml", true);
        xmlhttp.send();
    }

    // ajax function
    function ajaxState(xml) {
        var xmlDoc = xml.responseXML;
        var senators = []; // stores the updates senator list
        var senator = xmlDoc.getElementsByTagName("senator"); // gets xml list

        // loop through xml doc
        for (var i = 0; i < senator.length; i++) {
            var name = senator[i].getElementsByTagName("name")[0].childNodes[0].nodeValue;
            var party = senator[i].getElementsByTagName("party")[0].childNodes[0].nodeValue;

            // stores the name, party, and boolean
            var obj = {
                name: name,
                party: party,
                voted: false,
            };
            senators.push(obj); // adds to the senators list
            displaySenatorList(name, party, false); // call display function
        }
        msg.innerHTML = "From AJAX Loaded 10 senators";
        storeInLocalStorage(senators); // call to store in local storage
    }

    // display senator list
    function displaySenatorList(name, party) {
        var list = document.getElementById("members");
        var li = document.createElement("li");

        li.setAttribute("draggable", true);

        // sets color for democrat and republican
        if (party == "Democrat") {
            li.style.color = "blue";
        } else if (party == "Republican") {
            li.style.color = "red";
        }

        li.innerHTML = name;
        list.appendChild(li);
    }

    // store in local storage
    function storeInLocalStorage(senators) {
        var json = JSON.stringify(senators);
        var key = "senators";
        window.localStorage.setItem(key, json);
        addHandler();
    }

    // display senator list from local storage
    function displayFromLocalStorage(key) {
        for (var i = 0; i < key.length; i++) {
            var name = key[i].name;
            var party = key[i].party;
            var voted = key[i].voted;

            displaySenatorList(name, party);

            displayVotedSenators(name, party, voted)
            
        }
        document.getElementById("msg").innerHTML = "From LocalStorage Loaded 10 senators";
        addHandler();
    }

    // display senators who voted in box
    function displayVotedSenators(name, party, voted) {
        if (voted == true && party == "Democrat") {
            var list = document.getElementById("democrats");
            var li = document.createElement("li");
            li.innerHTML = name;
            list.appendChild(li);
        }
        if (voted == true && party == "Republican") {
            var list = document.getElementById("republicans");
            var li = document.createElement("li");
            li.innerHTML = name;
            list.appendChild(li);
        }
    }

    // intializes all the event handlerss
    function addHandler() {
        members = document.getElementById("members");
        members.ondragstart = dragStartHandler;
        members.ondragend = dragEndHandler;
        members.ondrag = dragHandler;

        targetDemocrat = document.getElementById("democrats");
        targetDemocrat.ondragenter = dragEnterDemocratsHandler;
        targetDemocrat.ondragover = dragEnterDemocratsHandler;
        targetDemocrat.ondragend = dragEnterDemocratsHandler;
        targetDemocrat.ondrop = dropDemocratsHandler;

        targetRepublican = document.getElementById("republicans");
        targetRepublican.ondragenter = dragEnterRepublicansHandler;
        targetRepublican.ondragover = dragEnterRepublicansHandler;
        targetRepublican.ondragend = dragEnterRepublicansHandler;
        targetRepublican.ondrop = dropRepublicansHandler;
    }

    function dragStartHandler(e) {
        document.getElementById("msg").innerHTML = "Dragging";
        sourceId = e.target.innerHTML;
        e.dataTransfer.setData("text/plain", sourceId);
    }

    function dragEndHandler(e) {
        document.getElementById("msg").innerHTML = "Drag ended";
    }

    function dragHandler(e) {
        msg.innerHTML = "Dragging " + e.target.innerHTML;
        e.preventDefault();
    }

    function dragEnterDemocratsHandler(e) {
        e.preventDefault();
    }

    // drop function for democrat
    function dropDemocratsHandler(e) {
        var list = document.getElementById("democrats");
        var li = document.createElement("li");

        var droppedDemocrat = e.dataTransfer.getData("text/plain", e.target.id);

        var key = JSON.parse(window.localStorage.getItem("senators"));

        // loop checks and display senators in box
        for (var i = 0; i < key.length; i++) {
            if (droppedDemocrat == key[i].name) {
                if (key[i].party == "Democrat") {
                    if (key[i].voted == false) {
                        if (droppedList.includes(droppedDemocrat) == false) {
                            li.innerHTML = droppedDemocrat;
                            list.appendChild(li);
                            droppedList.push(droppedDemocrat);
                            key[i].voted = true;
                            window.localStorage.setItem("senators", JSON.stringify(key));
                            break;
                        }
                    }
                }
            }
        }
    }

    function dragEnterRepublicansHandler(e) {
        e.preventDefault();
    }

     // drop function for republican
    function dropRepublicansHandler(e) {
        var list = document.getElementById("republicans");
        var li = document.createElement("li");

        var droppedRepublican = e.dataTransfer.getData("text/plain", e.target.id);

        var key = JSON.parse(window.localStorage.getItem("senators"));

        // loop checks and display senators in box
        for (var i = 0; i < key.length; i++) {
            if (droppedRepublican == key[i].name) {
                if (key[i].party == "Republican") {
                    if (key[i].voted == false) {
                        if (droppedList.includes(droppedRepublican) == false) {
                            li.innerHTML = droppedRepublican;
                            list.appendChild(li);
                            droppedList.push(droppedRepublican);
                            key[i].voted = true;
                            window.localStorage.setItem("senators", JSON.stringify(key));
                            break;
                        }
                    }
                }
            }
        }
    }
})();
