/** Original, deliberately non-predictive self-assessment helper. */
(function(root,factory){const api=factory();if(typeof module==='object'&&module.exports)module.exports=api;root.CareerMath=api;})(typeof globalThis!=='undefined'?globalThis:this,function(){'use strict';
function feedback(scores,labels){if(!Array.isArray(scores)||scores.length!==8||!scores.every(v=>Number.isInteger(v)&&v>=0&&v<=3))return {status:'invalid'};const names=Array.isArray(labels)&&labels.length===8?labels:['业务成果','客户价值','项目协作','团队管理','经营意识','决策质量','战略视野','治理与信任'];const entries=scores.map((v,i)=>({name:names[i],value:v,index:i}));entries.sort((a,b)=>a.value-b.value||a.index-b.index);return {status:'ok',gaps:entries.slice(0,2),unknown:entries.filter(x=>x.value===0).length,plain:'这是个人学习优先级提示，不是能力证明、职位预测或心理测量结果。'}}
function progress(done,all){if(!Array.isArray(all)||all.length===0)return 0;return all.filter(id=>!!done[id]).length/all.length*100}
return Object.freeze({feedback,progress});});
