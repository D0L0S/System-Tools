"============================================
"    Vim Configuration File
"    Written 13/05/2014
"============================================

" Automatic reloading of .vimrc
autocmd! bufwritepost .vimrc source %

" Search
nnoremap <silent> <Space> :silent noh<Bar>echo<CR> " Press space to clear search

" Better copy & paste
set pastetoggle=<F2>
set clipboard=unnamed

" Mouse and backspace
set mouse=a " on OSX ALT and click
set bs=2    " make backspace behave like normal again

" Rebinder <Leader> key
let mapleader = ','

" Quicksave command
noremap <C-Z> :update<CR>
vnoremap <C-Z> <C-C>:update<CR>
inoremap <C-Z> <C-O>:update<CR>

" Quick quit command
noremap <Leader>e :quit<CR> " Quit current window
noremap <Leader>E :qa!<CR>  " Quit ALL windows

" bind Ctrl+<movement> keys to move around the windows, instead of using Ctrl+w
" + <movement>
" " Every unnecessary keystroke that can be saved is good for your health :)
map <c-j> <c-w>j
map <c-k> <c-w>k
map <c-l> <c-w>l
map <c-h> <c-w>h

" Map sort function to a key
vnoremap <Leader>s :sort<CR>

" easier moving of code blocks
" " Try to go into visual mode (v), thenselect several lines of code here and
" " then press ``>`` several times.
vnoremap < <gv  " better indentation
vnoremap > >gv  " better indentation

" Enable syntax highlighting
" You need to reload this file for the change to apply
filetype off
filetype plugin indent on
syntax on

" Showing line numbers and length
set number  " show line numbers
set tw=79   " width of document (used by gd)
set nowrap  " don't automatically wrap on load
set fo-=t   " don't automatically wrap text when typing
set colorcolumn=80
highlight ColorColumn ctermbg=233

" Real programmers don't use TABs but spaces
" Mostly hear because Python cares on the type of white space
set tabstop=4
set softtabstop=4
set shiftwidth=4
set shiftround
set expandtab


"==================================================
"                       PLUGINS
"==================================================

" Setup Pathogen to manage your plugins
call pathogen#infect()

" NERDTree
map <C-n> :NERDTreeToggle<CR>
