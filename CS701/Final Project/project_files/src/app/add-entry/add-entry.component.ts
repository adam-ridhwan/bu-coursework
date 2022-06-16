import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';

import { Router } from '@angular/router';

@Component({
  selector: 'app-add-entry',
  templateUrl: './add-entry.component.html',
  styleUrls: ['./add-entry.component.css'],
})
export class AddEntryComponent implements OnInit {
  newEntries: any;

  // sets variables for JSON data
  constructor(private router: Router) {
    this.newEntries = new FormGroup({
      company: new FormControl(''),
      location: new FormControl(''),
      method: new FormControl(''),
      stage: new FormControl(''),
      position: new FormControl(''),
      type: new FormControl(''),
      date: new FormControl(''),
    });
  }

  ngOnInit(): void {
    console.log(
      JSON.parse(window.localStorage.getItem('amirhamzah_project') as string)
    );
  }

  cancel(): void {}

  // save to local storage
  save() {
    let key = JSON.parse(
      window.localStorage.getItem('amirhamzah_project') as string
    );

    if (key == null) {
      // sets default key to an empty array
      window.localStorage.setItem(
        'amirhamzah_project',
        JSON.stringify([this.newEntries.value])
      );
    } else {
      Object.values(this.newEntries.value).every((value) => {
        if (value === '') {
          // if the input fields are untouched and empty. nothing is done
          console.log('null entry');
        } else {
          // else, the input is stored into local storage
          key.splice(key.length, 0, this.newEntries.value);
          window.localStorage.setItem(
            'amirhamzah_project',
            JSON.stringify(key)
          );
          console.log(this.newEntries.value.company);
        }
      });
    }

    // resets input field and then navigates back to main page
    this.newEntries.reset();
    this.router.navigate(['']);
  }

  // clears the input field
  clear() {
    this.newEntries.reset();
  }
}
