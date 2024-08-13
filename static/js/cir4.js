$("document").ready(function () {

    //arrange blocks in a circle
    var block = $("#rotator #logo_a").get(),
        increase = Math.PI * 2 / block.length,
        x = 0, y = 0, angle = 0;

    for (var i = 0; i < block.length; i++) {
        var elem = block[i];
        x = 170 * Math.cos(angle) + 180;
        y = 170 * Math.sin(angle) + 180;
        elem.style.position = 'absolute';
        elem.style.left = x + 'px';
        elem.style.top = y + 'px';
        var rot = 90 + (i * (360 / block.length));
        angle += increase;
    }

    //arrange blocks in a circle
    // var block2 = $("#rotator #logo_b").get(),
    //     increase2 = Math.PI * 2 / block2.length,
    //     x2 = 0, y2 = 0, angle2 = 0;

    // for (var i = 0; i < block2.length; i++) {
    //     var elem2 = block2[i];
    //     x2 = 80 * Math.cos(angle2) + 90;
    //     y2 = 80 * Math.sin(angle2) + 90;
    //     elem2.style.position = 'absolute';
    //     elem2.style.left = x2 + 'px';
    //     elem2.style.top = y2 + 'px';
    //     var rot = 90 + (i * (360 / block2.length));
    //     angle2 += increase2;
    // }

    $('.btn_add').click(function () {
        let button = `<button class="btn btn-primary d_btn">d_btn</button>`;
        $('#demo').append(button);
    });

    // $('.d_btn').on('click', function () {
    //     alert('d_btn1');
    // });

    $(document).on('click', '.d_btn', function () {
        alert('d_btn2');
    });

});