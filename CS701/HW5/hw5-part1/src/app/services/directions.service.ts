import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root',
})
export class DirectionsService {
  constructor(private http: HttpClient) {}

  getDirection(from: string, to: string): Array<any> {
    let directionList: any[] = [];
    let url: string = `http://open.mapquestapi.com/directions/v2/route?key=Y6lk13ugbVXorNhtj5AOhDu0UZ0hBH2W&from=${from}&to=${to}`;

    this.http.get(url).subscribe(data);
    function data(data: any) {
      let maneuvers = data['route']['legs'][0]['maneuvers'];

      let maneuversList = [];

      for (var i in maneuvers) {
        let information = {
          narrative: maneuvers[i]['narrative'],
          distance: maneuvers[i]['distance'],
          mapUrl: maneuvers[i]['mapUrl'],
          iconUrl: maneuvers[i]['iconUrl'],
          order: parseInt(i) + 1,
        };
        maneuversList.push(information);
      }

      let obj = {
        distance: data['route']['distance'],
        time: data['route']['formattedTime'],
        detail: maneuversList,
      };

      directionList.push(obj);
    }
    return directionList;
  }
}
