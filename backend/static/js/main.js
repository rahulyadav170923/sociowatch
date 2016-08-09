//Follow Button Effect

var MainPage=React.createClass({
  render: function(){
    return (<div className="profile-container">
    lwkelswkelw<div>);
  }
});

ReactDOM.render(
  <MainPage />,
  document.getElementsByClassName('main-container')[0]
);



var Profile = React.createClass({
  render: function() {
    return (<div className="container">
		<header>
			<div className="bio">
        <img src="http://www.croop.cl/UI/twitter/images/up.jpg" alt="background" className="bg"/>
				<div className="desc">
					<h3>@carlf</h3>
					<p>Carl Fredricksen is the protagonist in Up. He also appeared in Dug </p>
				</div>
			</div>

			<div className="avatarcontainer">
				<img src="http://www.croop.cl/UI/twitter/images/carl.jpg" alt="avatar" className="avatar"/>
				<div className="hover">
						<div className="icon-twitter"></div>
				</div>
			</div>
		</header>

		<div className="content">
			<div className="data">
				<ul>
					<li>
						2,934
						<span>Tweets</span>
					</li>
					<li>
						1,119
						<span>Followers</span>
					</li>
					<li>
						530
						<span>Following</span>
					</li>
				</ul>
			</div>

			<div className="follow"> <div className="icon-twitter"></div> Follow</div>
		</div>

	</div>);
  }
});
/*
ReactDOM.render(
  <Profile />,
  document.getElementsByClassName('main-container')[0]
);*/
