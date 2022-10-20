import { Injectable } from '@angular/core';
import {HttpClient, HttpResponse, HttpHeaders} from "@angular/common/http";
import {any} from "codelyzer/util/function";



@Injectable({
  providedIn: 'root'
})
export class RabbitServiceService {


  constructor(private http: HttpClient) { }
  public  urlUpload = "http://localhost:15672/api/exchanges/%2f/amq.default/publish";
  public httpOptions = {
    headers: new HttpHeaders({
      'Content-Type':  'application/json',
      'Authorization': 'Basic ' + btoa('guest:guest')
    })
  };


  public uploadImage(name:string, bytes:string){
    let json = this.getUploadJson(name, bytes);
    this.http.post(this.urlUpload, JSON.stringify(json), this.httpOptions).subscribe(_=>
    {

    });
  }

  private getUploadJson(name:string, bytes:string){
    return <JSON><unknown>
        {
            "properties": {"delivery_mode": 2},
            "routing_key": "images_test",
            "content_type": "application/json",
            "payload":`{name: ${ name }, image: ${ bytes }`,
            "payload_encoding": "string"
        };

  }
}
