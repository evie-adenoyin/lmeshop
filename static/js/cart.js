console.log("hello world");
// Get customer token for fetch post method
function getToken(name) {
    var cookieValue = null;
    if(document.cookie && document.cookie !== ''){
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++){
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')){
                cookieValue =decodeURIComponent(cookie.substring(name.length +1));
                break;
            }
        }
    }
    return cookieValue
}

var csrftoken = getToken('csrftoken');


 // Add and remove from cart functionality with Fecth API

 var cartBtn = document.getElementsByClassName('addToCart')
 var user = '{{request.user}}'
 console.log(user);
 for (var i = 0; i < cartBtn.length; i++) {
     cartBtn[i].addEventListener('click', function(){
         var productID = this.dataset.product
         var action = this.dataset.action
         console.log(productID, action);
        
     if(user !== 'AnonymousUser'){
         UpdateUserCart(productID, action)
     }

 })

 }

 function UpdateUserCart(productID,action) {
     var url = '/lmeshop/update_cart/'

     fetch(url,{
         method: 'POST',
         headers: {
             "content-type": "application/json", 
             "X-CSRFToken": csrftoken,
         },
         body: JSON.stringify({'product': productID, 
                               'action': action})
              })
         .then((response)=>{
             return response.json
         })
         .then((data)=>{
             console.log(data);
             location.reload()
         })
 }

