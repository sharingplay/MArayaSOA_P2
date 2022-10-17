import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { LightgalleryModule } from 'lightgallery/angular';
import { HttpClientModule } from "@angular/common/http";

import { AppComponent } from './app.component';
import { LibraryComponent } from './components/library/library.component';
import { TopBarComponent } from './components/top-bar/top-bar.component';
import { UploadImagesComponent } from './components/upload-images/upload-images.component';

@NgModule({
  imports: [BrowserModule, FormsModule, LightgalleryModule, HttpClientModule],
  declarations: [AppComponent, LibraryComponent, TopBarComponent, UploadImagesComponent],
  bootstrap: [AppComponent]
})
export class AppModule {}
