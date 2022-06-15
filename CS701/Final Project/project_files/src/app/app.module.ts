import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ApplicationsComponent } from './applications/applications.component';
import { NoopAnimationsModule } from '@angular/platform-browser/animations';

import { MatIconModule } from '@angular/material/icon';
import { AddEntryComponent } from './add-entry/add-entry.component';

import { MatSelectModule } from '@angular/material/select';
import { DeleteEntryComponent } from './delete-entry/delete-entry.component';




@NgModule({
  declarations: [AppComponent, ApplicationsComponent, AddEntryComponent, DeleteEntryComponent],
  imports: [
    BrowserModule,
    FormsModule,
    ReactiveFormsModule,
    AppRoutingModule,
    NoopAnimationsModule,
    MatIconModule,
    MatSelectModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
