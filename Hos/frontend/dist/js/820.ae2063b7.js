"use strict";(self["webpackChunkfrontend"]=self["webpackChunkfrontend"]||[]).push([[820],{9820:function(t,e,r){r.r(e),r.d(e,{default:function(){return y}});var o=r(3396),n=r(7139);const a=(0,o._)("h1",{class:"topic"}," How would you like to pay? ",-1),c={class:"text-center"},i={class:"link-container"},s={key:0},l=(0,o._)("h2",null,"Order Details",-1),d={class:"text-center"};function u(t,e,r,u,h,_){const p=(0,o.up)("router-link");return(0,o.wg)(),(0,o.iD)("div",null,[a,(0,o._)("div",null,[(0,o._)("p",c," Please choose your payment method to pay $ "+(0,n.zw)(h.amount),1)]),(0,o._)("div",i,[(0,o.Wm)(p,{to:"UserCardPay",class:"link",onClick:e[0]||(e[0]=t=>_.to_bye_card(this.order))},{default:(0,o.w5)((()=>[(0,o.Uk)("Card")])),_:1}),(0,o._)("button",{class:"link",onClick:e[1]||(e[1]=t=>_.to_bye_cash(this.order))},"Cash"),(0,o.Wm)(p,{to:"userHelp",class:"link"},{default:(0,o.w5)((()=>[(0,o.Uk)("Help")])),_:1}),(0,o._)("button",{class:"link",onClick:e[2]||(e[2]=t=>_.show_order(h.order))},"Details"),h.bill.length>0?((0,o.wg)(),(0,o.iD)("div",s,[l,(0,o._)("ul",d,[((0,o.wg)(!0),(0,o.iD)(o.HY,null,(0,o.Ko)(h.bill,(t=>((0,o.wg)(),(0,o.iD)("li",{key:t.dish_name},(0,n.zw)(t.dish_name)+" - Qty: "+(0,n.zw)(t.dish_qty)+" - Price: "+(0,n.zw)(t.dish_price),1)))),128))])])):(0,o.kq)("",!0)])])}r(7658);var h=r(4161),_={data(){return{order:this.$route.params.order,amount:0,bill:[]}},created(){this.get_order_amount()},methods:{get_order_amount(){const t=`/api/function/get_order_amount/?order_code=${this.order}`;h.Z.get(t).then((t=>{this.amount=t.data.order_total_amount})).catch((t=>{console.error("Error fetching amount:",t)}))},to_bye_cash(t){this.$router.push("/userBye");const e=`/api/function/pay_cash/?order_code=${t}`;h.Z.get(e).then((()=>{alert("pay in: Cash")})).catch((t=>{console.error("Error fetching amount:",t)}))},to_bye_card(t){const e=`/api/function/pay_card/?order_code=${t}`;h.Z.get(e).then((()=>{alert("pay in: Card")})).catch((t=>{console.error("Error fetching amount:",t)}))},pay_bill(t){const e=`/api/function/pay_bill/?order_code=${t}`;h.Z.get(e).then((t=>{this.amount=t.data.order_amount})).catch((t=>{console.error("Error fetching amount:",t)}))},show_order(t){const e=`/api/function/show_bill/?order_code=${t}`;h.Z.get(e).then((t=>{this.bill=t.data})).catch((t=>{console.error("Error fetching amount:",t)}))}},mounted(){this.pay_bill(this.order)}},p=r(89);const m=(0,p.Z)(_,[["render",u]]);var y=m}}]);
//# sourceMappingURL=820.ae2063b7.js.map