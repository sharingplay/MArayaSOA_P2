import { Component, OnInit } from '@angular/core';
import {UploaderService} from "../../services/uploader.service";

@Component({
  selector: 'app-library',
  templateUrl: './library.component.html',
  styleUrls: ['./library.component.css']
})
export class LibraryComponent implements OnInit {

  constructor(public service: UploaderService) { }

  public images: string[] = []
  transform480 = [{ height: "480", width: "480" }];
  transform800 = [{ height: "800", width: "800" }];
  transform1400 = [{ height: "1400", width: "1400" }];

  ngOnInit(): void {
    this.service.getImages().subscribe(data =>
        this.images = data['images']);;
  }

}
