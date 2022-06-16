var animModule = (function () {
    window.onload = init;

    var canvas;
    var context;
    var width, height;

    var ballRadius = 10;
    var ballColor = "blue";
    var ballPosition;
    var angle = 0;

    // displacement of ball for each step
    var dx = 5;

    function init() {
        canvas = document.getElementById("testCanvas");
        context = canvas.getContext("2d");

        width = canvas.width;
        height = canvas.height;

        // current ball position
        ballPosition = { x: ballRadius, y: ballRadius + 5 };
    }

    function setSpeed(speed) {
        let newSpeed = +speed;
        if (dx > 0) dx = newSpeed;
        else dx = -newSpeed;
    }

    // draw current position on the canvas
    function drawBallOnCanvas() {
        // Clear the canvas

        context.fillStyle = "#D3C0C0";
        context.fillRect(0, 0, canvas.width, canvas.height);

        // Fill in the rest of the code

        /*
        Two functions are created for the program: -
        1) drawLines() - draws the lines on the canvas
        2) circle() - creates the circle object and moves it
         */

        function drawLines() {
            context.strokeStyle = "#000000"; // this is line color
            context.lineWidth = 2; // this is thickness of line
            let leftSide = 25; // value of left y axis
            let rightSide = 50; // value of right y axis

            for (let i = 0; i < 16; i++) {
                // for-loop used to draw lines
                context.beginPath();
                if (i % 2 == 0) {
                    // if index is EVEN, lines are drawn from left wall
                    context.moveTo(0, leftSide);
                    context.lineTo(380, leftSide);
                    leftSide = leftSide + 50;
                } else {
                    // if index is ODD, lines are drawn from right wall
                    context.moveTo(405, rightSide);
                    context.lineTo(25, rightSide);
                    rightSide = rightSide + 50;
                }
                context.stroke();
                context.closePath();
            }
        }
        drawLines();

        function circle() {
            context.beginPath();
            context.arc(ballPosition.x, ballPosition.y, ballRadius, 0, 2 * Math.PI, true); // this creates the circle

            if (angle % 2 == 0) {
                // if angle is EVEN
                context.fillStyle = ballColor; // set ball to blue
                if (ballPosition.x <= width) {
                    // if x value of ballPosition is less than width
                    ballPosition.x = ballPosition.x + dx; // value is incremented by dx
                    if (ballPosition.x > width) {
                        // if x value of ballPosition is greater than width (reaches the wall)
                        ballPosition.y = ballPosition.y + 25; // y value is incremented by 25, which places ball to the next floor
                        angle++; // angle is incremented
                    }
                }
            }

            if (angle % 2 == 1) {
                // if angle is ODD
                context.fillStyle = "#FF0000"; // set ball to red
                if (ballPosition.x >= 0) {
                    // if x value of ballPosition is more than or equal to 0
                    ballPosition.x = ballPosition.x - dx; // value is decremented by dx
                    if (ballPosition.x < 0) {
                        // if x value of ballPosition is less than 0 (reaches the wall)
                        ballPosition.y = ballPosition.y + 25; // y value is incremented by 25, which places ball to the next floor
                        angle++; // angle is incremented
                    }
                }
            }

            if (ballPosition.y > height) {
                // resetting values and places ball to the intial start position
                ballPosition.y = 15;
                angle = 0;
            }

            context.fill();
            context.closePath();
        }
        circle();
    }

    // browser specific animation request
    window.requestAnimFrame = (function () {
        return (
            window.requestAnimationFrame ||
            window.webkitRequestAnimationFrame ||
            window.mozRequestAnimationFrame ||
            window.oRequestAnimationFrame ||
            window.msRequestAnimationFrame ||
            // fall back to JavaScript setTimeout
            function (callback, element) {
                window.setTimeout(callback, 1000 / 60);
            }
        );
    })();

    // Define the Animation
    function doAnimation() {
        // Draw a single frame of animation on our canvas
        drawBallOnCanvas();

        // After this frame is drawn, let the browser schedule the next one

        window.requestAnimFrame(doAnimation);
    }

    // Start the Animation

    window.requestAnimFrame(doAnimation);

    return {
        setSpeed: setSpeed,
    };
})();
