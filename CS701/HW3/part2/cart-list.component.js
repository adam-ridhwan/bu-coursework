angular.module("cartApp").component("cartList", {
    templateUrl: "cart-list/cart-list.template.html",
    controller: function CartListController() {
        var key = JSON.parse(window.localStorage.getItem("amirhamzah_cart"));
        if (key == "" || key == undefined) {
            this.defaultBooks = [
                { title: "Absolute Java", qty: 1, price: 114.95 },
                { title: "Pro HTML5", qty: 2, price: 27.95 },
                { title: "Head First HTML5", qty: 1, price: 27.89 },
            ];
        } else {
            this.defaultBooks = key;
        }

        // removes book from list
        this.removeBook = function (index) {
            this.defaultBooks.splice(index, 1);
        };

        // adds book to list
        this.addBook = function () {
            this.defaultBooks.splice(this.defaultBooks.length, 0, { title: "New Book", qty: 1, price: 10.99 });
        };

        // saves book to local storage
        this.saveBooks = function () {
            window.localStorage.setItem("amirhamzah_cart", JSON.stringify(this.defaultBooks));
        };

        // updates total amount
        this.updateTotal = function () {
            var total = 0;

            angular.forEach(this.defaultBooks, function (value) {
                total += value.qty * value.price;
            });

            return total;
        };
    },
});
