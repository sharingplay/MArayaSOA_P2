import { Component, VERSION, ViewEncapsulation } from "@angular/core";
import lgZoom from 'lightgallery/plugins/zoom';
import { BeforeSlideDetail } from 'lightgallery/lg-events';
import {RabbitServiceService} from './services/rabbit-service.service'



@Component({
  selector: "my-app",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.css"],
  encapsulation: ViewEncapsulation.None
})
export class AppComponent {
  title = 'Angular Material 12 Image Upload with Preview';
  name = "Angular " + VERSION.major;
  fileSelected = "No file selected";
  fileName = "No file selected";
  settings = {
    counter: false,
    plugins: [lgZoom]
  };
  constructor(private rabbitService: RabbitServiceService) {}
  onBeforeSlide = (detail: BeforeSlideDetail): void => {
    const { index, prevIndex } = detail;
    console.log(index, prevIndex);
  };

  onFileSelect(input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = (e: any) => {
        this.fileName = input.files[0].name;
        this.fileSelected = e.target.result;
      }
      reader.readAsDataURL(input.files[0]);
    }
  }

  uploadFiles(){
      this.rabbitService.uploadImage(this.fileName, this.fileSelected);
  }
}
