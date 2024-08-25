$(document).ready(function () {

    // Handling successful query sent alert(start)

    $('.message-sent-successful-alert-cancel-btn').click(function(){
        $('.message-sent-successful-alert').fadeOut('slow')
    })

    setTimeout(function(){
        $('.message-sent-successful-alert').fadeOut('slow')
    }, 3000)

    // Handling successful query sent alert(end)

    // Handling comment submission (start)

    $('.comment-submit-btn').click(function(){
        const commentSubmitButton = $(this);
        commentSubmitButton.hide();

        $('.comment-submit-loading-btn').show();

        const usersComment = $('.users-comment-box-text-area').val();
        const blogId = $('.blog_id_input').val();

        const data = {
            'comment': usersComment,
            'blogId': blogId
        }

        $('.users-comment-box-text-area').val('');

        $.post('/comments/user-comment', data, function(response){
            const res = JSON.parse(response);

            const allComments = res.all_comments;

             console.log(allComments);

            if(res.code){
                $('.comment-submit-loading-btn').hide();

                let commentsHtml = ``

                $.each(allComments, function(_, value){
                    commentsHtml += `<div class="other-users-comment mb-2">
                                        <div class="other-users-identity mb-2">
                                            <div class="other-users-image">
                                                <img src="/web/image/res.users/${value.user_id}/image_1920" alt="logged-in user"/>
                                            </div>
                                            <h6 class="other-users-name">
                                                ${value.user_name}
                                            </h6>
                                        </div>
                                        <p class="other-users-comment-text">
                                            <i class="fa-solid fa-message"></i>
                                            ${value.comment}
                                        </p>
                                    </div>`
                })

                $('.other-users-comment-container').empty();
                if(allComments.length > 5){
                     $('.other-users-comment-container').append(`<button type="button" class="comment-see-more-btn mt-2">See more</button>`)
                }
                $('.other-users-comment-container').prepend(commentsHtml);

                const singleCommentHtml = `<div class="other-users-comment mb-2">
                                        <div class="other-users-identity mb-2">
                                            <div class="other-users-image">
                                                <img src="/web/image/res.users/${allComments[0].user_id}/image_1920" alt="logged-in user"/>
                                            </div>
                                            <h6 class="other-users-name">
                                                ${allComments[0].user_name}
                                            </h6>
                                        </div>
                                        <p class="other-users-comment-text">
                                            <i class="fa-solid fa-message"></i>
                                            ${allComments[0].comment}
                                        </p>
                                    </div>`

                $('.all-other-users-comment-container').prepend(singleCommentHtml);

                commentSubmitButton.show();
            }
        })
    })

    $(document).on('click', '.comment-see-more-btn', function(){
        $('.other-users-comment-container').hide('slow');
        $('.all-other-users-comment-container').show('slow');
    })

    $(document).on('click', '.comment-see-less-btn', function(){
        $('.all-other-users-comment-container').hide('slow');
        $('.other-users-comment-container').show('slow');
    })

    // Handling comment submission (end)

    // Handling scroll to top button (start)

    let scrollButtonParent = $('.scroll-to-top-btn-parent');

    $(window).on('scroll', function() {
        if ($(this).scrollTop() > 300) {
            scrollButtonParent.fadeIn();
        } else {
            scrollButtonParent.fadeOut();
        }
    });

    $('.scroll-to-top-button').on('click', function() {
        $('html, body').animate({ scrollTop: 0 }, 'slow');
        return false;
    });

    // Handling scroll to top button (end)

});
