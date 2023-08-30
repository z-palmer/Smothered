document.addEventListener('DOMContentLoaded', function () {

    insta_widget();

});

function insta_widget() {

    // fetches Instagram API data from Smothered account
    var key = process.env.IG_API_KEY
    fetch(`https://graph.instagram.com/me/media?fields=id,media_type,media_url,permalink,thumbnail_url,timestamp&access_token=${key}`)
        .then(response => response.json())
        .then(posts => {
            console.log(posts);
            // get last nine posts
            const grid = posts.data.slice(-9);
            console.log(grid);
            grid.forEach(element => {
                var grid_pic;
                if (element.media_type == 'VIDEO') {
                    grid_pic = document.createElement('video');
                    grid_pic.setAttribute('class', 'insta-grid-vid');
                    grid_pic.setAttribute('controls', '');
                } else {
                    grid_pic = document.createElement('img');
                    grid_pic.setAttribute('class', 'insta-grid-pic');
                }
                const grid_preview = document.createElement('div');
                const preview_link = document.createElement('a');
                preview_link.setAttribute('href', element.permalink);
                grid_preview.setAttribute('class', 'insta-grid-preview');
                grid_pic.setAttribute('src', element.media_url);
                preview_link.append(grid_pic);
                grid_preview.append(preview_link);
                document.getElementById('instagram-widget').append(grid_preview);
            });
        });
}