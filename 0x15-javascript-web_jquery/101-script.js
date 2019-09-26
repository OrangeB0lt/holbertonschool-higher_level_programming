window.onload = function () {
  $('DIV#add_item').click(function () {
    const thing = '<li>Item</li>';
    $('UL.my_list').append(thing);
  });
  $('DIV#remove_item').click(function () {
    $('UL.my_list > li').last().remove();
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list > li').remove();
  });
};
