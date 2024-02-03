import { Component } from '@angular/core';
import axios from "axios";

@Component({
  selector: 'app-root',
  template: `
   <div class="container">
    <p class="title-text"> Summarizer</p>
     <textarea class="textarea" [(ngModel)]="text" placeholder="Enter text to summarize..." spellcheck="false"> </textarea>
     <label for="select"> Select AI model </label>
     <select name="select" [(ngModel)]="model">
       <option value="facebook/bart-large-cnn">facebook/bart-large-cnn</option>
       <option value="pszemraj/led-base-book-summary">pszemraj/led-base-book-summary</option>
       <option value="Falconsai/text_summarization">Falconsai/text_summarization</option>
     </select>
     <button (click)="summarize()"> Summarize </button>
     <p class="result" *ngIf="isloading"> Generating summary....</p>
     <p class="result" *ngIf="summaryIsDone"> Summary: {{result}}</p>
   </div>
  `,
  styles: []
})
export class AppComponent {
  title = 'nai'
  text = '';
  model = 'facebook/bart-large-cnn';
  result = '';
  summaryIsDone = false;
  isloading = false;
  summarize(){
    this.summaryIsDone = false;
    this.isloading = true;
    axios.post('http://127.0.0.1:5000/api/summarize', {
      model: this.model,
      text_to_summarize: this.text
    }).then((response) => {
      console.log(response.data)
      this.result = response.data.summary
    }).finally(() => {
      this.isloading = false;
      this.summaryIsDone = true;
    })
  }

}
