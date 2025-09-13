customColorPalette = [
    {'color': 'hsl(4, 90%, 58%)', 'label': 'Red'},
    {'color': 'hsl(340, 82%, 52%)', 'label': 'Pink'},
    {'color': 'hsl(291, 64%, 42%)', 'label': 'Purple'},
    {'color': 'hsl(262, 52%, 47%)', 'label': 'Deep Purple'},
    {'color': 'hsl(231, 48%, 48%)', 'label': 'Indigo'},
    {'color': 'hsl(207, 90%, 54%)', 'label': 'Blue'},
]

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': {
            'items': [
                'heading', '|',
                'bold', 'italic', 'underline', 'strikethrough', 'highlight', '|',
                'link', '|',
                'alignment', '|',
                'bulletedList', 'numberedList', 'todoList', '|',
                'imageUpload', 'insertTable', 'mediaEmbed', '|',
                'removeFormat', 'sourceEditing'
            ],
            'shouldNotGroupWhenFull': True,
        },
        'alignment': {
            'options': ['left', 'center', 'right', 'justify']
        },
        'language': 'en'
    },

    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3', '|',
            'bulletedList', 'numberedList', '|', 'blockQuote'
        ],
        'toolbar': {
            'items': [
                'heading', '|',
                'outdent', 'indent', '|',
                'bold', 'italic', 'underline', 'strikethrough', '|',
                'code', 'codeBlock', '|',
                'subscript', 'superscript', '|',
                'alignment', '|',
                'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', '|',
                'imageUpload', 'insertImage', 'insertTable', 'mediaEmbed', '|',
                'removeFormat', 'sourceEditing'
            ],
            'shouldNotGroupWhenFull': True,
        },
        'alignment': {
            'options': ['left', 'center', 'right', 'justify']
        },
        'image': {
            'toolbar': [
                'imageTextAlternative', '|',
                'imageStyle:alignLeft', 'imageStyle:alignCenter', 'imageStyle:alignRight', 'imageStyle:side'
            ],
            'styles': ['full', 'side', 'alignLeft', 'alignRight', 'alignCenter']
        },
        'table': {
            'contentToolbar': [
                'tableColumn', 'tableRow', 'mergeTableCells',
                'tableProperties', 'tableCellProperties'
            ],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            }
        },
        'heading': {
            'options': [
                {'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph'},
                {'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1'},
                {'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2'},
                {'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3'},
            ]
        }
    },

    'list': {
        'properties': {
            'styles': True,
            'startIndex': True,
            'reversed': True,
        }
    }
}

CKEDITOR_5_FILE_UPLOAD_PERMISSION = "authenticated"

