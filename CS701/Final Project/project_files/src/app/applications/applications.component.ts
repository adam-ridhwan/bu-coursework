import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-applications',
  templateUrl: './applications.component.html',
  styleUrls: ['./applications.component.css'],
})
export class ApplicationsComponent implements OnInit {
  defaultEntries: Array<any>; // default array

  constructor() {
    let key = JSON.parse(
      window.localStorage.getItem('amirhamzah_project') as string
    );
    if (key != null) {
      this.defaultEntries = key;
    } else {
      this.defaultEntries = [];
    }
  }

  ngOnInit(): void {
    let key = JSON.parse(
      window.localStorage.getItem('amirhamzah_project') as string
    );
    if (key == null) {
      window.localStorage.setItem('amirhamzah_project', JSON.stringify([]));
    }

    // delete empty fields
    this.deleteEmptyEntries(key);
  }

  // save all entries
  saveEntry(): void {
    window.localStorage.setItem(
      'amirhamzah_project',
      JSON.stringify(this.defaultEntries)
    );
  }

  /* 
  is user saves an empty field after clearing the input fields. 
  then deleteEmptyEntries() function is performed
   */
  deleteEmptyEntries(key: string | any[]) {
    for (let i = 0; i < key.length; i++) {
      Object.values(key[i]).every((value) => {
        if (value === null || value === undefined || value === '') {
          this.defaultEntries.splice(i, 1);
          window.localStorage.setItem(
            'amirhamzah_project',
            JSON.stringify(this.defaultEntries)
          );
        }
      });
    }
  }
}
