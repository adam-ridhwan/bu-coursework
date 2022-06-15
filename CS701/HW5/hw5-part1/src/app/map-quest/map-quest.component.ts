import { Component, OnInit } from '@angular/core';
import { DirectionsService } from '../services/directions.service';

@Component({
  selector: 'app-map-quest',
  templateUrl: './map-quest.component.html',
  styleUrls: ['./map-quest.component.css'],
  providers: [DirectionsService]
})
export class MapQuestComponent implements OnInit {
  from: string;
  to: string;
  directionList: Array<any> = [];

  constructor(private directionsService: DirectionsService) {
    this.from = 'Boston, MA';
    this.to = 'Cambridge, MA';
  }

  ngOnInit(): void {}

  get(): void {
    this.directionList = [];
    this.directionList = this.directionsService.getDirection(
      this.from,
      this.to
    );
    console.log(this.directionList);
  }
}
