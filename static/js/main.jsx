
var MyBox = MyBox || {};
Route = ReactRouter.Route;
RouteHandler = ReactRouter.RouteHandler;
DefaultRoute = ReactRouter.DefaultRoute;
Link = ReactRouter.Link;
State = ReactRouter.State;

Mybox.Link = React.createClass({
  render: function() {
    return <ReactRouter.Link
      activeClassName="pure-button-active"
      to={this.props.to} >{this.children}</ReactRouter.Link>
  }
});

MyBox.App = React.createClass({
  mixins: [State],
  render: function () {
    return (
      <div className="content pure-g">
        <div className="pure-menu pure-menu-open pure-menu-horizontal pure-u-1">
          <h3>MyBox</h3>
          <ul>
            <li><MyBox.Link to="mail">Inbox</MyBox.Link></li>
            <li><MyBox.Link to="about">About</MyBox.Link></li>
          </ul>
        </div>
        <RouteHandler/>
      </div>
      );
  }
});

MyBox.Mail = React.createClass({
  mixins: [State],
  render: function () {
    return (
      <div className="pure-u-1">
        <p>wut</p>
      </div>
    );
  }
});


MyBox.About = React.createClass({
  mixins: [State],
  render: function() {
    return (
      <div className="pure-u-1">
        <h2>MyBox</h2>
        <p>A Personal Mailbox</p>
        <p>Mailbox aims to help you with yor mail</p>
      </div>
    )
  }
})


MyBox.Actions = Reflux.createActions([
  'openPath', 'closePath',
  'openMail', 'closeMail',
  ]);

MyBox.Routes = (
    <Route handler={MyBox.App}>
      <Route name="mail"  handler={MyBox.Mail} />
      <Route name="about"  handler={MyBox.About} />
    </Route>
    )


ReactRouter.run(MyBox.Routes, function (Handler) {
  React.render(<Handler/>, document.body);
});

