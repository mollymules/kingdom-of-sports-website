$(document).ready(
		function(){
			$('#slideshow').innerfade({
				speed: 'slow',
				timeout: 4000,
				type: 'sequence',
				containerheight: '320px'
			});
			$('#soccer').popover({selector: "a[rel=popover]"});
			$('#football').popover({selector: "a[rel=popover]"});
			$('#tennis').popover({selector: "a[rel=popover]"});
			$('#golf-putting').popover({selector: "a[rel=popover]"});
			$('#golf-pitching').popover({selector: "a[rel=popover]"});
		}
	);


function getFacebookAlbums(){
$(document).ready(function() {
  var albumIdsUrl = "https://graph.facebook.com/275078275954895/albums?callback=?";
  var dudAlbums = ["Untitled Album", "Profile Pictures","Cover Photos","Mobile Uploads","Timeline Photos", "3D View"]
  $.getJSON(albumIdsUrl, function(data) {
       var len = data.data.length;
       var legitAlbumCount = 0;
       for(var i=0;i<len;i++){
            var aid = data.data[i].id;
            var albumName = data.data[i].name;
            if($.inArray(albumName, dudAlbums) == -1){
            	getAlbumCoverPhoto(data.data[i].cover_photo, aid, albumName, data.data[i].count, legitAlbumCount);
            	legitAlbumCount++;
            }
       }
    }); 

});
}

function getAlbumCoverPhoto(coverPhoto, albumId, albumName, albumCount, iCount) {
	var coverPhotoUrl = "https://graph.facebook.com/" + coverPhoto + "?callback=?";
	$.getJSON(coverPhotoUrl, function(coverPhotoData) {
		if(typeof(coverPhotoData.picture)!="undefined"){
			htmlData = '<div class="col-md-6 text-center singleFbAlbum"><figure><a href="' + coverPhotoData.link + '"><img class="img-responsive" src="' + coverPhotoData.picture + '" /></a></figure><figcaption>'+albumName+'</br>'+albumCount+' Photos</figcaption></div>';  
			$('#fbAlbums').append(htmlData);    
		}  	
	});    	    
}  