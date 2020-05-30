import Buefy from 'buefy';
import Vue from 'vue';
import { VueMasonryPlugin } from 'vue-masonry';
import VueI18n from 'vue-i18n';
import VueAnalytics from 'vue-analytics';
import App from './App.vue';
import router from './router';
import setUpAxiosCsrfConfig from './components/utils/csrf';
import './registerServiceWorker';

Vue.config.productionTip = false;
Vue.use(Buefy);
Vue.use(VueMasonryPlugin);
Vue.use(VueI18n);
setUpAxiosCsrfConfig();
Vue.use(VueAnalytics, {
  id: 'UA-125854450-3',
  router,
});

function getBrouserLang(defaultValue) {
  const langClip = navigator.language.substr(0, 2); // 获取浏览器配置语言前两位;

  if (langClip !== '') {
    return langClip;
  }
  return defaultValue;
}

const i18n = new VueI18n({
  // locale: 'en_US',
  locale: getBrouserLang('zh'), // 语言标识 默认中文
  messages: {
    zh: require('./assets/lang/zh'), // 中文语言包
    en: require('./assets/lang/en'), // 英文语言包
    ja: require('./assets/lang/ja'), // 英文语言包
  },
});

Vue.filter('formatDate', (value, fmt) => {
  const getDate = new Date(value);
  const o = {
    'M+': getDate.getMonth() + 1,
    'd+': getDate.getDate(),
    'h+': getDate.getHours(),
    'm+': getDate.getMinutes(),
    's+': getDate.getSeconds(),
    'q+': Math.floor((getDate.getMonth() + 3) / 3),
    S: getDate.getMilliseconds(),
  };
  if (/(y+)/.test(fmt)) {
    // eslint-disable-next-line no-param-reassign
    fmt = fmt.replace(RegExp.$1, (`${getDate.getFullYear()}`).substr(4 - RegExp.$1.length));
  }
  // eslint-disable-next-line no-restricted-syntax
  for (const k in o) {
    if (new RegExp(`(${k})`).test(fmt)) {
      // eslint-disable-next-line no-param-reassign
      fmt = fmt.replace(RegExp.$1, (RegExp.$1.length === 1) ? (o[k]) : ((`00${o[k]}`).substr((`${o[k]}`).length)));
    }
  }
  return fmt;
});

Vue.filter('formatNum', (num) => {
  if (num >= 1000000) {
    return `${(num / 1000000).toFixed(1).replace(/.0$/, '')}w`;
  }
  if (num >= 1000) {
    return `${(num / 1000).toFixed(1).replace(/.0$/, '')}k`;
  }
  return num;
});

new Vue({
  router,
  i18n,
  render: h => h(App),
}).$mount('#app');
