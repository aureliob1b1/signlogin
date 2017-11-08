$('#toggle-box-checkbox').on('change', function(){
  if(this.checked){
    $('body').addClass('night');
  }else{
    $('body').removeClass('night');
  }
});
