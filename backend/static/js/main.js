//Follow Button Effect
var Profile = React.createClass({
  onError() {
  this.src=this.props.profile_image
},
  render: function() {
    return (<div className="container">
		<header>
			<div className="bio">
        <img src={this.props.background ? this.props.background:"http://abs.twimg.com/images/themes/theme1/bg.png"} alt='no banner'  className="bg"/>
				<div className="desc">
					<h3>@{this.props.twitter_handle}</h3>
					<p>{this.props.description}</p>
				</div>
			</div>
			<div className="avatarcontainer">
				<img src={this.props.profile_image} alt="avatar" className="avatar"/>
				<div className="hover">
						<div className="icon-twitter"></div>
				</div>
			</div>
		</header>
		<div className="content">
			<div className="data">
				<ul>
					<li>
						{this.props.tweets}
						<span>Tweets</span>
					</li>
					<li>
						{this.props.followers}
						<span>Followers</span>
					</li>
					<li>
						{this.props.following}
						<span>Following</span>
					</li>
				</ul>
			</div>

			<div className="follow"> <div className="icon-twitter"></div> {this.props.twitter_handle}</div>
		</div>

	</div>);
  }
});
/*
var profiles=[]
for (var i = 0; i < 8; i++) {
  profiles.push(<Profile />)
}
*/

var MainPage=React.createClass({
  getInitialState: function() {
    return {profiles:[]};
  },
  componentDidMount:function(){
    this.serverRequest=$.get('/profiles',function (result) {
      var profiles=[]
      for (var i = 0; i < 8; i++) {
        profiles.push(<Profile background={result[i]['profile_banner_url']} twitter_handle={result[i]['screen_name']}
        description={result[i]['description']} tweets={result[i]['statuses_count']} followers={result[i]['followers_count']}
        following={result[i]['friends_count']} profile_image={result[i]['profile_image_url']}/>)
      }
      this.setState({profiles:profiles})
    }.bind(this))
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
);
var profiles=[]
for (var i = 0; i < 8; i++) {
  profiles.push(<Profile background={data[i]['profile_background_image_url']}/>)
}
*/
