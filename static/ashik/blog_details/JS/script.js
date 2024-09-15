$(document).ready(function () {

    // --------------------OLD CODE-------------------------

     // Handling successful query sent alert(start)

     /* $('.message-sent-successful-alert-cancel-btn').click(function(){
         $('.message-sent-successful-alert').fadeOut('slow')
     })

     setTimeout(function(){
         $('.message-sent-successful-alert').fadeOut('slow')
     }, 3000) */

     // Handling successful query sent alert(end)

    // --------------------OLD CODE-------------------------

    // Handling query form submission AJAX (start)

    $('.form-submit-btn').click(function(){

        if($('#name-input').val().trim() === ''){
            $('.no-name-warning').fadeIn('slow');
            $('#name-input').focus();
            return;
        }

        else {
            $('.no-name-warning').fadeOut('slow');
        }

        if($('#email-input').val().trim() === ''){
            $('.no-email-warning').fadeIn('slow');
            $('#email-input').focus();
            return;
        }

        else {
            $('.no-email-warning').fadeOut('slow');
        }

        $('.form-submit-btn').hide();

        $('.query-submit-loading-btn').show();

        //$("body").css("overflow", "hidden");

        $('.user-query-form').hide();

        $('.thanks-div').show();

        const nameInput = $('#name-input').val();
        const emailInput = $('#email-input').val();
        const mobileInput = $('#mobile-input').val();
        const blogID = $('#blog-id').val();

        const data = {
            nameInput, emailInput, mobileInput, blogID
        }

        $('#name-input').val('');
        $('#email-input').val('');
        $('#mobile-input').val('');

        $.post('/query/user-query', data, function(response){
            const res = JSON.parse(response);

            if(res.code === 200){
                $('.payment-success-btn').click(function(){
                    //$("body").css("overflow", "auto");
                    $('.thanks-div').hide();
                    $('.user-query-form').show();
                })

                $('.form-submit-btn').show();

                $('.query-submit-loading-btn').hide();
            }
        })
    })



    // Handling query form submission AJAX (end)

    // Handling comment submission (start)

    $('.comment-submit-btn').click(function(){
        if($('.users-comment-box-text-area').val().trim() === ''){
            $('.no-comment-warning').fadeIn('slow');
            $('.users-comment-box-text-area').focus();
            return;
        }

        else{
            $('.no-comment-warning').fadeOut('slow');
        }

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

            const allComments = res.all_comments_l_5;
            const totalNumberOfComments = res.total_number_of_comments;

            console.log(allComments);

            if(res.code){
                $('.comment-submit-loading-btn').hide();

                $('.number-of-comments').empty();

                $('.number-of-comments').text(totalNumberOfComments);

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
                if(totalNumberOfComments > 5){
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
