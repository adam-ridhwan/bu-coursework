angular.module("myApp", []).controller("CartControler", function ($scope) {
    var undoHistory = []; // stores undo objects
    var redoHistory = []; // stores redo objects

    // gets item from local storage or from initial list
    var key = JSON.parse(window.localStorage.getItem("amirhamzah_cart"));
    if (key == "" || key == undefined) {
        $scope.defaultBooks = [
            { title: "Absolute Java", qty: 1, price: 114.95 },
            { title: "Pro HTML5", qty: 2, price: 27.95 },
            { title: "Head First HTML5", qty: 1, price: 27.89 },
        ];
    } else {
        $scope.defaultBooks = key;
    }

    // sets redo and redo buttons to
    $scope.undoDisabled = true;
    $scope.redoDisabled = true;

    // removes book to list
    $scope.removeBook = function (index) {
        var removedBook = $scope.defaultBooks.splice(index, 1);

        undoHistory.push(removedBook[0]);

        printer();
        checker();
    };

    // adds book to list
    $scope.addBook = function () {
        var newBook = { title: "New Book", qty: 1, price: 10.99 };

        $scope.defaultBooks.splice($scope.defaultBooks.length, 0, newBook);

        undoHistory.push(newBook);

        printer();
        checker();
    };

    // saves list of books to local storage
    $scope.saveBooks = function () {
        window.localStorage.setItem("amirhamzah_cart", JSON.stringify($scope.defaultBooks));
    };

    // updates the total amount
    $scope.updateTotal = function () {
        $scope.$watch(function () {
            $scope.total = 0;
            angular.forEach($scope.defaultBooks, function (value) {
                $scope.total += value.qty * value.price;
            });
        });
    };

    // undo function
    $scope.undo = function () {
        var undoHistoryLastItem = undoHistory[undoHistory.length - 1];
        var defaultBooksLastItems = $scope.defaultBooks[$scope.defaultBooks.length - 1];

        if (undoHistoryLastItem == defaultBooksLastItems) {
            var item = undoHistory.pop();
            $scope.defaultBooks.pop();
            redoHistory.push(item);
        } else if (undoHistoryLastItem != defaultBooksLastItems) {
            var item = undoHistory.pop();
            $scope.defaultBooks.push(item);
            redoHistory.push(item);
        }

        printer();
        checker();
    };

    // redo function
    $scope.redo = function () {
        var redoHistoryLastItem = redoHistory[redoHistory.length - 1];
        var defaultBooksLastItems = $scope.defaultBooks[$scope.defaultBooks.length - 1];

        if (redoHistoryLastItem != defaultBooksLastItems) {
            var item = redoHistory.pop();
            $scope.defaultBooks.push(item);
            undoHistory.push(item);
        } else if (redoHistoryLastItem == defaultBooksLastItems) {
            var item = redoHistory.pop();
            $scope.defaultBooks.pop(item);
            undoHistory.push(item);
        }

        printer();
        checker();
    };

    // enables or disables button function
    function checker() {
        if (undoHistory.length == 0) {
            $scope.undoDisabled = true;
        } else {
            $scope.undoDisabled = false;
        }

        if (redoHistory.length == 0) {
            $scope.redoDisabled = true;
        } else {
            $scope.redoDisabled = false;
        }
    }

    // prints undo list, redo and displayed list in console
    function printer() {
        console.log(" ");
        console.log("undo history", undoHistory);
        console.log("redo history", redoHistory);
        console.log("storage", $scope.defaultBooks);
    }
});
