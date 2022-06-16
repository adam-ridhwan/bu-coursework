import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-part2',
  templateUrl: './part2.component.html',
  styleUrls: ['./part2.component.css']
})
export class Part2Component implements OnInit {
  input: any;     // sets input variable
  delimiter: any; // sets delimiter variable 

  constructor() { 
    this.input = "Angular is awesome" // default text
    this.delimiter = "#"              // default symbol
  }

  ngOnInit(): void {
  }

}
