import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { ApplicationsComponent } from './applications/applications.component';
import { AddEntryComponent } from './add-entry/add-entry.component';
import { DeleteEntryComponent } from './delete-entry/delete-entry.component';

const routes: Routes = [
  { path: '', component: ApplicationsComponent },
  { path: 'add', component: AddEntryComponent },
  { path: 'delete/:company', component: DeleteEntryComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
