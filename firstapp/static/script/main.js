window.onload=function(){
  var labArr = $(".ui.right.ribbon.label");
  var segArr = $(".ui.container.segment.stag");
  for(var i=0; i<labArr.length; i++)
  {

    if(/[t][e][c][h]/.test(labArr.eq(i).html())==true)
    {
      labArr.eq(i).addClass('blue');
      segArr.eq(i).addClass('blue');
    }
    if(/[l][i][f][e]/.test(labArr.eq(i).html())==true)
    {
      labArr.eq(i).addClass('red');
      segArr.eq(i).addClass('red');
    }
  }
}
