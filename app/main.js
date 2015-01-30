
import {Router} from 'aurelia-router';

export class App {
  static inject() {
    return [Router];
  }
  constructor(router) {
    this.router = router;
    this.router.configure(config => {
      config.title = 'MyBox';
      config.map([
        { route: ['','about'], moduleId: 'about', nav: true, title:'About'},
      ]);
    });
  }
}
