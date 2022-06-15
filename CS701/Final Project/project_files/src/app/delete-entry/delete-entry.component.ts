import { Component, OnInit } from '@angular/core';

import { ActivatedRoute } from '@angular/router';
import { Router } from '@angular/router';

@Component({
  selector: 'app-delete-entry',
  templateUrl: './delete-entry.component.html',
  styleUrls: ['./delete-entry.component.css'],
})
export class DeleteEntryComponent implements OnInit {
  selection!: string;

  constructor(private route: ActivatedRoute, private router: Router) {}

  ngOnInit(): void {
    // gets the index of array using the value of company
    let index = this.route.snapshot.params['company'];
    this.selection = index;

    console.log(index);
  }

  // delete entry
  delete() {
    let key = JSON.parse(
      window.localStorage.getItem('amirhamzah_project') as string
    );

    // saves to local storage
    for (let i = 0; i < key.length; i++) {
      if (key[i].company == this.selection) {
        key.splice(i, 1);
        window.localStorage.setItem('amirhamzah_project', JSON.stringify(key));
        console.log('deleted successfully');
      }
    }
    this.router.navigate(['']);
  }
}
