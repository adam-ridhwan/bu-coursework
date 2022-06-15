angular.module("myApp", []).controller("CartControler", function ($scope) {
    var key = JSON.parse(window.localStorage.getItem("amirhamzah_cart"));
    if (key == "" || key == undefined) {
        var defaultBooks = [
            { title: "Absolute Java", qty: 1, price: 114.95 },
            { title: "Pro HTML5", qty: 2, price: 27.95 },
            { title: "Head First HTML5", qty: 1, price: 27.89 },
        ];
        $scope.defaultBooks = defaultBooks;
    } else {
        $scope.defaultBooks = key;
    }

    // removes book from list
    $scope.removeBook = function (index) {
        $scope.defaultBooks.splice(index, 1);
    };

    // add book from list
    $scope.addBook = function () {
        $scope.defaultBooks.splice($scope.defaultBooks.length, 0, { title: "New Book", qty: 1, price: 10.99 });
    };

    // saves book to local storage
    $scope.saveBooks = function () {
        window.localStorage.setItem("amirhamzah_cart", JSON.stringify($scope.defaultBooks));
    };

    // updates total amount
    $scope.updateTotal = function () {
        $scope.$watch(function () {
            $scope.total = 0;
            angular.forEach($scope.defaultBooks, function (value) {
                $scope.total += value.qty * value.price;
            });
        });
    };
});
