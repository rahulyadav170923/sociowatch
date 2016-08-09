//Follow Button Effect
var Profile = React.createClass({
  render: function() {
    return (<div className="container">
		<header>
			<div className="bio">
        <img src={this.props.background} alt="background" className="bg"/>
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


var MainPage=React.createClass({
  getInitialState: function() {
    $.get('http://127.0.0.1:5000/profiles',function (data) {
      var profiles=[]
      for (var i = 0; i < 8; i++) {
        profiles.push(<Profile background={data[i]['profile_background_image_url']}/>)
      }
      return {'profiles':profiles};
    })
  },
  render: function(){
    return (<div className="profile-container">
    {this.state.profiles}
    </div>);
  }
});

ReactDOM.render(
  <MainPage />,
  document.getElementsByClassName('main-container')[0]
);


/*
ReactDOM.render(
  <Profile />,
  document.getElementsByClassName('main-container')[0]
);*/
