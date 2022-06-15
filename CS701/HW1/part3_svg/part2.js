var rotationsModule = (function () {
    function changeSpeed() {
        var duration = document.getElementById("duration").value;
        document.getElementById("durationDisplay").value = duration + "s";

        // Fill in the rest of the code to change the dur attributes of the four animations

		var yeet = document.getElementById("speed"); // gets the element object 
        yeet.setAttribute("dur", duration + "s"); // sets the duration attribute with duration variable
    }

    return {
        changeSpeed: changeSpeed,
    };
})();
