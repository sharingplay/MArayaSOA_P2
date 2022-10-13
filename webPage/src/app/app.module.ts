import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { LightgalleryModule } from 'lightgallery/angular';

import { AppComponent } from './app.component';
import { LibraryComponent } from './components/library/library.component';
import { TopBarComponent } from './components/top-bar/top-bar.component';

@NgModule({
  imports: [BrowserModule, FormsModule, LightgalleryModule],
  declarations: [AppComponent, LibraryComponent, TopBarComponent],
  bootstrap: [AppComponent]
})
export class AppModule {}
