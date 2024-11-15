	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 15, 0
	.globl	_main                           ; -- Begin function main
	.p2align	2
_main:                                  ; @main
	.cfi_startproc
; %bb.0:                                ; %main_entry
	sub	sp, sp, #16
	.cfi_def_cfa_offset 16
	mov	w8, #50                         ; =0x32
	mov	w9, #45                         ; =0x2d
	mov	w0, #69                         ; =0x45
	stp	w9, w8, [sp, #8]
	add	sp, sp, #16
	ret
	.cfi_endproc
                                        ; -- End function
.subsections_via_symbols
