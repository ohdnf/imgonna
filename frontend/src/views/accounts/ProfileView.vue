<template>
  <div>
    <div class="container profile">
      <div class="row">
        <div class="span12">
          <div class="well well-small clearfix">
            <div class="row-fluid">
              <div class="span2">
                <img src="http://www.gravatar.com/avatar/f6112e781842d6a2b4636b35451401ff?s=125" class="img-polaroid"/>         
              </div>
              <div class="span4">
                <h2>Jonnie Spratley</h2> 
                <ul class="unstyled">
                  <li><i class="icon-phone"></i> 916-241-3613</li>
                  <li><i class="icon-envelope"></i> jonniespratley@me.com</li>
                  <li><i class="icon-globe"></i> http://jonniespratley.me</li>
                </ul>
              </div>
              <div class="span6">
              <ul class="inline stats">
                  <li>
                    <span>275</span>
                    Friends
                  </li>
                  <li>
                    <span>354</span>
                    Followers
                  </li>
                  <li>
                    <span>186</span>
                    Photos
                  </li>
              </ul>
                <div><!--/span6-->
                </div><!--/row-->
              </div>
            </div>
          <!--Body content-->
          </div>
        </div>
      </div>
    </div> 
    <div class="well clearfix">
      <img class="pull-right" src="http://kcdn3.klout.com/static/images/developers/dev-assets/powered-by-klout.png" width="150px"/>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProfileView"
};
</script>

<style scoped>
body{
  padding-top:25px !important;
}
.stats {
  text-align:center;
  text-shadow:1px 1px 0px #fff;
  margin-top:25px;  
  
}
.stats li{
  width:125px; 
}
.stats span{
  font-family:Helvetica;
  font-weight:bold;
  text-shadow:1px 1px 0px #fff;
  font-size:4em;
  
  display:block;
  line-height:1em;
}

/* Large desktop */
@media (min-width: 1200px) { 
}
 
/* Portrait tablet to landscape and desktop */
@media (min-width: 768px) and (max-width: 979px) { 
}
 
/* Landscape phone to portrait tablet */
@media (max-width: 767px) { 
  .profile img{
    width:75px;
  }
  .profile h2{
    font-size:1.7em;
  }
  .stats span{
    font-size: 2em;
  }
}
 
/* Landscape phones and down */
@media (max-width: 480px) { 
}
</style>