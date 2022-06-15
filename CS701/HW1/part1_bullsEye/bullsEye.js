var bullsEyeModule = (function () {
    window.onload = init;

    // canvas and context variables
    var canvas;
    var context;

    // center of the pattern
    var centerX, centerY;

    var delay = false;

    // Interval
    var timerId;

    function init() {
        canvas = document.getElementById("testCanvas");
        context = canvas.getContext("2d");

        centerX = canvas.width / 2;
        centerY = canvas.height / 2;

        // draw the initial pattern
        drawPattern();
    }

    // called whenever the slider value changes or the delay checkbox is clicked
    function drawPattern() {
        if (timerId) {
            clearInterval(timerId);
            timerId = undefined;
        }

        context.clearRect(0, 0, canvas.width, canvas.height);

        var bandWidth = document.getElementById("band").value;
        document.getElementById("widthDisplay").value = bandWidth;

        delay = document.getElementById("delay").checked;

        // Fill in the rest of the code

        /*
        3 functions created: -
        1) drawCircles() - draws circles on canvas
        2) delayedCircles() - draws circles on canvas incrementally
        3) main() - runs entire program with drawCircles() and delayed Circles()
        */

        let size = 200; // stores ength of arc
        let index = 0; // stores index of each circle
        let redCircle = "#FF0000"; // stores hex value of red
        let blueCircle = "#0000FF"; // stores hex value of blue

        function drawCircles() {
            if (index % 2 == 0) {
                // if index is even, red circle is drawn
                context.fillStyle = redCircle;
            } else {
                // else index is odd, blue circle is drawn
                context.fillStyle = blueCircle;
            }
            context.beginPath();
            context.arc(centerX, centerY, size, 0, 2 * Math.PI, true);
            context.closePath();
            context.fill();
            index++;
            size = size - bandWidth;
        }

        function delayedCircles() {
            setTimeout(function () {
                if (size > 0) {
                    // while size does not equal to zero, a circle is drawn with a recursive call after
                    drawCircles();
                    delayedCircles(); // recursive call
                }
            }, 1500);
        }

        function main() {
            if (delay == true) {
                // if delayed checkbox is clicked, delayedCircles() is called
                delayedCircles();
            } else {
                // else, drawCircles() is called
                while (size > 0) {
                    drawCircles();
                }
            }
        }
        main();
    }

    return {
        drawPattern: drawPattern,
    };
})();
