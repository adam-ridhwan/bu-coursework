import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-part1',
  templateUrl: './part1.component.html',
  styleUrls: ['./part1.component.css'],
})
export class Part1Component implements OnInit {
  defaultBooks: Array<any>;
  total!: number;

  constructor() {
    let key = JSON.parse(
      window.localStorage.getItem('amirhamzah_cart') as string
    );
    if (key != null) {
      this.defaultBooks = key;
    } else {
      this.defaultBooks = [
        { title: 'Absolute Java', qty: 1, price: 114.95 },
        { title: 'Pro HTML5', qty: 2, price: 27.95 },
        { title: 'Head First HTML5', qty: 1, price: 27.89 },
      ];
    }
  }

  ngOnInit() {}

  // remove book from list
  removeBook(index: number) {
    this.defaultBooks.splice(index, 1);
  }

  // add book to list
  addBook(): void {
    this.defaultBooks.splice(this.defaultBooks.length, 0, {
      title: 'New Book',
      qty: 1,
      price: 10.99,
    });
  }

  // save book to local storage
  saveBooks(): void {
    window.localStorage.setItem(
      'amirhamzah_cart',
      JSON.stringify(this.defaultBooks)
    );
  }

  // update total price
  updateTotal(): number {
    this.total = 0;
    for (let i = 0; i < this.defaultBooks.length; i++) {
      this.total += this.defaultBooks[i].qty * this.defaultBooks[i].price;
    }
    return this.total;
  }
}
