Prism.languages.cilkcpp = Prism.languages.insertBefore('cpp', 'function', {
    'parallel-keyword': {
        pattern: /\bcilk_(?:for|reducer|s(?:cope|pawn|ync))\b/,
        alias: 'keyword'
    }
});

Prism.languages['cilk-cpp'] = Prism.languages['cilkcpp'];
Prism.languages['cilk'] = Prism.languages['cilkcpp'];
