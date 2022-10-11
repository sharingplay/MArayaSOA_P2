import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { LightgalleryModule } from 'lightgallery/angular';

import { AppComponent } from './app.component';

@NgModule({
  imports: [BrowserModule, FormsModule, LightgalleryModule],
  declarations: [AppComponent],
  bootstrap: [AppComponent]
})
export class AppModule {}
