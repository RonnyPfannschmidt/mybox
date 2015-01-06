
var MyBox = MyBox || {};
Route = ReactRouter.Route;
RouteHandler = ReactRouter.RouteHandler;
DefaultRoute = ReactRouter.DefaultRoute;
Link = ReactRouter.Link;


MyBox.startup = function(div) {
  var routes = MyBox.Routes();
  ReactRouter.run(routes, function (Handler) {
    React.render(<Handler/>, document.body);
  });

};
MyBox.App = React.createClass({
  render: function () {
    return (
      <div className="content pure-g">
        <div className="pure-menu pure-menu-open pure-u-1">
          <Link className="pure-menu-title" to="app">MyBox</Link>
          <ul>
            <li><Link to="app">Inbox</Link></li>
          </ul>
        </div>
        <RouteHandler/>
      </div>
      );
  }
});

MyBox.Dashboard = React.createClass({
  render: function () {
    return (
      <div className="pure-u-1">
        <p>wut</p>
      </div>
    );
  }
});

MyBox.Actions = Reflux.createActions([
  'openPath', 'closePath',
  'openMail', 'closeMail',
  ]);

MyBox.Routes = function() {

  return (
    <Route name='app' path='/' handler={MyBox.App}>
      <DefaultRoute handler={MyBox.Dashboard}/>
    </Route>
    )
};


MyBox.startup(document.body);
