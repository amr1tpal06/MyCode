import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MatButtonModule } from '@angular/material/button';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatCardModule } from '@angular/material/card';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './components/header/header.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  imports: [MatButtonModule, MatToolbarModule, MatCardModule, HttpClientModule, CommonModule, HeaderComponent],
  standalone: true,
})
export class AppComponent implements OnInit { //something wrong with this code
  title = 'my-angular-project';
  books: any[] = [];

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.http.get<any[]>('http://127.0.0.1:5000/')  
      .subscribe(
        response => {
          this.books = response;
        }
      );
  }
}

//learn angular 18 and then code this properly - services etc 
// plan out the application and then 