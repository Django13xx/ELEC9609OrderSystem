"use strict";(self["webpackChunkfrontend"]=self["webpackChunkfrontend"]||[]).push([[192],{2192:function(e,t,s){s.r(t),s.d(t,{default:function(){return V}});var a=s(3396),n=s(7139),i=s(9242);const r=e=>((0,a.dD)("data-v-c5ba77ce"),e=e(),(0,a.Cn)(),e),c=r((()=>(0,a._)("div",null,[(0,a._)("h5",{class:"custom-menu-intro"},[(0,a.Uk)(" LEFT: Menu View "),(0,a._)("br"),(0,a.Uk)(" RIGHT: Sopping Cart "),(0,a._)("br"),(0,a._)("br"),(0,a.Uk)(' "+" to add Dish '),(0,a._)("br"),(0,a.Uk)(' "-" to delete dish '),(0,a._)("br"),(0,a.Uk)(" Place order when ready "),(0,a._)("br"),(0,a._)("br"),(0,a.Uk)(" Try AI generating menu "),(0,a._)("br"),(0,a.Uk)(" Have fun with HOS! ")])],-1))),l={class:"custom-price text-center"},o=r((()=>(0,a._)("br",null,null,-1))),d={class:"col-md-4 table-container-cart"},h=r((()=>(0,a._)("h2",{class:"table-name"},"Shopping Cart",-1))),u={class:"table table-bordered table-hover table-header"},_=r((()=>(0,a._)("thead",null,[(0,a._)("th",{class:"text-center sticky-header"},"Name"),(0,a._)("th",{class:"text-center sticky-header"},"Price"),(0,a._)("th",{class:"text-center sticky-header"},"Qty"),(0,a._)("th",{class:"text-center sticky-header"},"Add"),(0,a._)("th",{class:"text-center sticky-header"},"Delete")],-1))),m={class:"text-center dish_name"},p={class:"text-center"},b={class:"text-center"},g={class:"text-center"},k=["onClick"],f=r((()=>(0,a._)("i",{class:"fa fa-plus"},null,-1))),y=[f],v={class:"text-center"},C=["onClick"],w=r((()=>(0,a._)("i",{class:"fa fa-minus"},null,-1))),x=[w],M={class:"col-md-6 offset-md-4 table-container-menu"},D=r((()=>(0,a._)("h2",{class:"table-name"},"Main Menu",-1))),U={class:"table table-bordered table-hover table-header"},q=r((()=>(0,a._)("thead",null,[(0,a._)("th",{class:"text-center sticky-header"},"Name"),(0,a._)("th",{class:"text-center sticky-header"},"Type"),(0,a._)("th",{class:"text-center sticky-header"},"Pic"),(0,a._)("th",{class:"text-center sticky-header"},"Price"),(0,a._)("th",{class:"text-center sticky-header"},"Edit")],-1))),A={class:"text-center dish_name"},I={class:"text-center"},P={class:"text_center"},T=["src"],$={class:"text-center"},z={class:"text-center"},S=["onClick"],E=r((()=>(0,a._)("i",{class:"fa fa-plus"},null,-1))),H=[E],Z={class:"chat-interface"},N={class:"input-container"},Q={class:"chat-display"},B={class:"message"},O={class:"link-container"};function K(e,t,s,r,f,w){const E=(0,a.up)("h7"),K=(0,a.up)("router-link");return(0,a.wg)(),(0,a.iD)("div",null,[c,(0,a._)("div",null,[(0,a._)("p",l,[(0,a.Uk)("Total Price: "),o,(0,a.Uk)("$"+(0,n.zw)(w.totalCartPrice),1)]),(0,a._)("div",d,[h,(0,a._)("table",u,[_,(0,a._)("tbody",null,[((0,a.wg)(!0),(0,a.iD)(a.HY,null,(0,a.Ko)(f.cart,(e=>((0,a.wg)(),(0,a.iD)("tr",{key:e.id},[(0,a._)("td",m,(0,n.zw)(e.name),1),(0,a._)("td",p,(0,n.zw)(e.price),1),(0,a._)("td",b,(0,n.zw)(e.qty),1),(0,a._)("td",g,[(0,a._)("button",{class:"btn",onClick:t=>w.increaseQuantity(e)},y,8,k)]),(0,a._)("td",v,[(0,a._)("button",{class:"btn",onClick:t=>w.decreaseQuantity(e)},x,8,C)])])))),128))])])]),(0,a._)("div",M,[D,(0,a._)("table",U,[q,(0,a._)("tbody",null,[((0,a.wg)(!0),(0,a.iD)(a.HY,null,(0,a.Ko)(f.menus,(e=>((0,a.wg)(),(0,a.iD)("tr",{key:e.dish_id},[(0,a._)("td",A,(0,n.zw)(e.dish_name),1),(0,a._)("td",I,(0,n.zw)(e.dish_type),1),(0,a._)("td",P,[(0,a._)("img",{src:`/api/static/images/${e.dish_name}.jpg`,alt:"Dish Image"},null,8,T)]),(0,a._)("td",$,(0,n.zw)(e.dish_price),1),(0,a._)("td",z,[(0,a._)("button",{class:"btn",onClick:t=>w.addToCart(e)},H,8,S)])])))),128))])])]),(0,a._)("div",Z,[(0,a._)("div",N,[(0,a.wy)((0,a._)("input",{"onUpdate:modelValue":t[0]||(t[0]=e=>f.inputMessage=e),onKeyup:t[1]||(t[1]=(0,i.D2)(((...e)=>w.sendMessage&&w.sendMessage(...e)),["enter"])),placeholder:"Get help from AI services..."},null,544),[[i.nr,f.inputMessage]]),(0,a._)("button",{onClick:t[2]||(t[2]=(...e)=>w.sendMessage&&w.sendMessage(...e))},"Send")]),(0,a._)("div",Q,[(0,a.Wm)(E,null,{default:(0,a.w5)((()=>[(0,a.Uk)(" HOS Chatbot (Chatgpt): ")])),_:1}),(0,a._)("div",B,(0,n.zw)(f.message),1)])])]),(0,a._)("div",O,[(0,a._)("button",{class:"custom_remove_all menulink link",onClick:t[3]||(t[3]=(...e)=>w.remove_all&&w.remove_all(...e))},"Clear Cart"),(0,a.Wm)(K,{to:{name:"orderSuccess"},class:"menuLink customRouterOrder",onClick:w.saveAndNavigate},{default:(0,a.w5)((()=>[(0,a.Uk)("Place Order")])),_:1},8,["onClick"]),f.showButton?((0,a.wg)(),(0,a.iD)("button",{key:0,onClick:t[4]||(t[4]=(...e)=>w.autoDish&&w.autoDish(...e)),class:"menuLink customButton blinking-button"},"AI MENU")):(0,a.kq)("",!0)])])}s(7658);var L=s(4161),F={name:"UserMenuPage",data(){return{base_url:"/api/menu/",menus:null,url:"",dish_id:"",dish_name:"",dish_type:"",dish_pic:"",dish_price:"",dish_qty:"",cart:[],showButton:!1,number:this.$route.params.number,table:this.$route.params.table,order:this.$route.params.order,amount:0,dishes:[],inputMessage:"",messages:[],message:""}},created(){setTimeout((()=>{this.showButton=!0}),1e3)},computed:{totalCartPrice(){const e=this.cart.reduce(((e,t)=>e+t.qty*t.price),0);return e.toFixed(2)}},methods:{saveAndNavigate(){for(const t of this.cart)L.Z.post("/api/orderContent/",{order:this.order,dish_name:t.name,dish_qty:t.qty}).then((e=>{console.log("order content create successfully",e.data)})).catch((e=>{console.error("order content create failed",e)}));this.amount=this.totalCartPrice;const e=`/api/function/order_unpaid/?order_code=${this.order}&total_amount=${this.amount}`;L.Z.get(e).then((()=>{console.log("Axios Success:",e)})).catch((e=>{console.error("Axios Error:",e)}))},autoDish(){const e=`/api/function/auto_dish/?people_number=${this.number}`;L.Z.get(e).then((e=>{this.dishes=e.data,this.cart=[];for(const t of this.dishes){const e=this.findMenuInstance(t);if(e)for(let s=0;s<t.dish_qty;s++)this.addToCart(e)}})).catch((e=>{console.error("Error fetching dishes:",e)}))},findMenuInstance(e){for(const t of this.menus)if(t.dish_name===e.dish_name)return t;return null},getAll(){L.Z.get(this.base_url).then((e=>{this.menus=e.data,this.url="",this.dish_id="",this.dish_name="",this.dish_type="",this.dish_pic="",this.dish_price="",this.dish_qty=""}))},addToCart(e){const t=this.cart.find((t=>t.name===e.dish_name));if(t)t.qty++;else{const t=this.cart.length+1;this.cart.push({id:t,name:e.dish_name,price:e.dish_price,qty:1})}},increaseQuantity(e){e.qty++},decreaseQuantity(e){if(e.qty>1)e.qty--;else{const t=this.cart.findIndex((t=>t.id===e.id));-1!==t&&this.cart.splice(t,1)}},remove_all(){this.cart=[]},sendMessage(){if(""===this.inputMessage.trim())return;const e=`/api/function/ai_services/?statement=${this.inputMessage}`;L.Z.get(e).then((e=>{e.data&&e.data.message?this.message=e.data.message:alert("Invalid response data")})).catch((e=>{console.error("Error:",e)})),this.inputMessage=""}},mounted(){this.getAll()}},G=s(89);const R=(0,G.Z)(F,[["render",K],["__scopeId","data-v-c5ba77ce"]]);var V=R}}]);
//# sourceMappingURL=192.39cc4700.js.map