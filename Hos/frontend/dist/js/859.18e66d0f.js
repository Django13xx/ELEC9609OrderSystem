"use strict";(self["webpackChunkfrontend"]=self["webpackChunkfrontend"]||[]).push([[859],{6859:function(t,e,n){n.r(e),n.d(e,{default:function(){return M}});var a=n(3396),l=n(7139);const o={class:"container mt-5 text-center"},s={class:"row justify-content-center"},i={class:"col-md-6"},r=(0,a._)("h2",null,"ADMIN MODE",-1),c={class:"mb-4"},u=(0,a._)("h4",null,"Total Revenue",-1),d={class:"mb-4 link-container"},h={class:"mb-3"},m={class:"mb-3"},g={class:"mb-3"},_={key:0},k=(0,a._)("h2",null,"Order Details",-1),v={class:"text-center"},f={class:"mb-3 link-container"};function b(t,e,n,b,w,p){const D=(0,a.up)("RouterLink");return(0,a.wg)(),(0,a.iD)("div",o,[(0,a._)("div",s,[(0,a._)("div",i,[r,(0,a._)("div",c,[u,(0,a._)("p",null,(0,l.zw)(w.totalRevenue),1)]),(0,a._)("div",d,[(0,a._)("div",h,[(0,a.Wm)(D,{to:"containerMenu",class:"btn link"},{default:(0,a.w5)((()=>[(0,a.Uk)("Manage all Menus")])),_:1})]),(0,a._)("div",m,[(0,a.Wm)(D,{to:"adminTable",class:"btn link"},{default:(0,a.w5)((()=>[(0,a.Uk)("Manage all Tables")])),_:1})]),(0,a._)("div",g,[(0,a._)("button",{onClick:e[0]||(e[0]=(...t)=>p.orderDetails&&p.orderDetails(...t)),class:"btn link"},"View historical Orders")])]),w.order.length>0?((0,a.wg)(),(0,a.iD)("div",_,[k,(0,a._)("ul",v,[((0,a.wg)(!0),(0,a.iD)(a.HY,null,(0,a.Ko)(w.order,(t=>((0,a.wg)(),(0,a.iD)("li",{key:t.dish_name,style:{"list-style":"none"}},(0,l.zw)(t.dish_name)+" - Quantity Sold: "+(0,l.zw)(t.dish_qty),1)))),128))])])):(0,a.kq)("",!0),(0,a._)("div",f,[(0,a._)("button",{onClick:e[1]||(e[1]=(...t)=>p.goBack&&p.goBack(...t)),class:"btn link"},"Log Out")])])])])}n(7658);var w=n(4161),p={data(){return{totalRevenue:0,order:[],admin:this.$route.params.admin}},methods:{orderDetails(){const t="/api/function/get_all_orders/";w.Z.get(t).then((t=>{this.order=t.data})).catch((t=>{console.error("Error fetching amount:",t)}))},goBack(){const t="/api/function/logout/";w.Z.get(t,{params:{admin:this.admin}}).then((t=>{console.log(t),!0===t.data.success?(this.$router.push({name:"hosWelcome"}),alert("admin "+this.admin+" logout successfully!")):alert("logout failed, please try again")})).catch((t=>{console.log(t)}))}},mounted(){const t="/api/function/get_total_revenue/";w.Z.get(t).then((t=>{this.totalRevenue=t.data.totalRevenue})).catch((t=>{console.error("Error fetching amount:",t)}))}},D=n(89);const y=(0,D.Z)(p,[["render",b]]);var M=y}}]);
//# sourceMappingURL=859.18e66d0f.js.map