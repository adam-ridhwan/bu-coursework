import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'tokenizer',
})
export class TokenizerPipe implements PipeTransform {
  transform(value: any, args?: any): any {
    let delimiter = args;
    let result: string = '';

    for (let i = 0; i < value.length; i++) {
      if (delimiter == null) {
        delimiter = ',';
      }
      result = result + value[i] + delimiter;
    }
    return result;

    console.log(value);
    console.log(args) 
  }
}
